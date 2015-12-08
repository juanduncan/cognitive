/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_COWN_MISC_ADC_TAGS_GEN_H
#define INCLUDED_COWN_MISC_ADC_TAGS_GEN_H

#include <COWN_misc/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace COWN_misc {

    /*!
     * \brief <+description of block+>
     * \ingroup COWN_misc
     *
     */
    class COWN_MISC_API adc_tags_gen : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<adc_tags_gen> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of COWN_misc::adc_tags_gen.
       *
       * To avoid accidental use of raw pointers, COWN_misc::adc_tags_gen's
       * constructor is in a private implementation
       * class. COWN_misc::adc_tags_gen::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace COWN_misc
} // namespace gr

#endif /* INCLUDED_COWN_MISC_ADC_TAGS_GEN_H */

